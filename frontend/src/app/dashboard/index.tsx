"use client";
import React, { useState } from "react";
import styles from '@/app/utils/css/dash/dashboard.module.css';

interface DashboardProps {}

const Dashboard: React.FC<DashboardProps> = () => {
  const [teaDropdownOpen, setTeaDropdownOpen] = useState(false);
  const [cargoDropdownOpen, setCargoDropdownOpen] = useState(false);
  const [reportsDropdownOpen, setReportsDropdownOpen] = useState(false);

  return (
    <div className={styles.body}>
      <nav className={styles.nav_bar}>
        <div className={styles.search}>
          <input type="search" placeholder="Search..." />
          <button>Search</button>
        </div>
      </nav>

      <aside className={styles.side}>
        <ul>
          <li onMouseEnter={() => setTeaDropdownOpen(true)} onMouseLeave={() => setTeaDropdownOpen(false)}>
            Tea
            {teaDropdownOpen && (
              <ul className={styles.dropdown}>
                <li>Receive Consignment</li>
                <li>Receive Tea</li>
                <li>Release Tea</li>
              </ul>
            )}
          </li>
          <li onMouseEnter={() => setCargoDropdownOpen(true)} onMouseLeave={() => setCargoDropdownOpen(false)}>
            Cargo
            {cargoDropdownOpen && (
              <ul className={styles.dropdown}>
                <li>Receive Consignment</li>
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
        <h1>Welcome to Dynamike Dashboard</h1>
        {/* Your dashboard widgets or data visualizations go here */}
      </main>
    </div>
  );
};

export default Dashboard;
