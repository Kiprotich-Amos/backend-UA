"use client";
import React, { use, useState } from "react";
import styles from '@/app/utils/css/dash/dashboard.module.css';
import Cargo from "@/app/dashboard/(general-cargo)/cargo";
import TeaReceiving from '@/app/dashboard/(tea-app)/receiving-tea';
import Container from "@/app/dashboard/(con)/consignment";


interface DashboardProps {}

const Dashboard: React.FC<DashboardProps> = () => {
  const [teaDropdownOpen, setTeaDropdownOpen] = useState(false);
  const [cargoDropdownOpen, setCargoDropdownOpen] = useState(false);
  const [reportsDropdownOpen, setReportsDropdownOpen] = useState(false);
  const [cargoReceiveDisplay, setCargoReceiveDisplay] = useState(false);
  const [teaReceivingDisplay, setTeaReceivingDisplay] = useState(false);
  const [containerDisplay, setContainerDisplay] = useState(false)

  return (
    <div className={styles.body}>
      <nav className={styles.nav_bar}>
        <div className={styles.search}>
          <input type="search" placeholder="Search..." />
          <button>Search</button>
        </div>
      </nav>

      <aside className={styles.side}>
        <ul className={styles.menu}>
          <li>Home</li>
          <li onClick={()=>{setContainerDisplay(true);setTeaReceivingDisplay(false); setCargoReceiveDisplay(false)}}>Receive Consignment</li>
          <li onMouseEnter={() => setTeaDropdownOpen(true)} onMouseLeave={() => setTeaDropdownOpen(false)}>
            Tea
            {teaDropdownOpen && (
              <ul className={styles.dropdown}>
                <li onClick={()=>{setContainerDisplay(false);setTeaReceivingDisplay(true); setCargoReceiveDisplay(false)}}>Receive Tea</li>
                <li>Release Tea</li>
              </ul>
            )}
          </li>
          <li onMouseEnter={() => setCargoDropdownOpen(true)} onMouseLeave={() => setCargoDropdownOpen(false)}>
            Cargo
            {cargoDropdownOpen && (
              <ul className={styles.dropdown}>
                <li onClick={()=>{setContainerDisplay(false);setTeaReceivingDisplay(false); setCargoReceiveDisplay(true)}}>Receive Consignment</li>
                <li>Release Cargo</li>
              </ul>
            )}
          </li>
          <li onMouseEnter={() => setReportsDropdownOpen(true)} onMouseLeave={() => setReportsDropdownOpen(false)}>
            Reports
            {reportsDropdownOpen && (
              <ul className={styles.dropdown}>
                <li>Storage Report</li>
                <li>Activity Logs</li>
              </ul>
            )}
          </li>
          <li>Users</li>
          <li>Settings</li>
        </ul>
      </aside>
      <main className={styles.main_content}>
        <div className={styles.consignmentReceiving}>
          { cargoReceiveDisplay && <Cargo />}
        </div>
        <div className="styles.consignmentReceiving">
          {teaReceivingDisplay && <TeaReceiving/>}
        </div>
        <div className="styles.consignmentReceiving">
          {containerDisplay && <Container/>}
        </div>
      </main>
    </div>
  );
};

export default Dashboard;
