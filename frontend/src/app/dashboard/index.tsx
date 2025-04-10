"use client";
import React, { useState } from "react";
import styles from '@/app/utils/css/dash/dashboard.module.css';

interface DashboardProps{};

const Dashboard : React.FC<DashboardProps> = () =>{
    const [teaDropdownOpen, setTeaDropdownOpen] = useState(false);
    const [cargoDropdownOpen, setCargoDropdownOpen] = useState(false);
    const [reportsDropdownOpen, setReportsDropdownOpen] = useState(false);
    return(
        <>
            <nav className={styles.nav_bar}>
                <div className={styles.search}>
                    <search>
                        <input type="search-text" placeholder="Search..." />
                        <button>Search</button>
                    </search>
                </div>
            </nav>
            <aside className={styles.side}>
                <ul>
                    <li  onMouseEnter={() =>setTeaDropdownOpen(true)} onMouseLeave={() => setTeaDropdownOpen(false)}>
                        Tea
                        {teaDropdownOpen && (
                            <ul className={styles.dropdown}>
                                <li>Receive Consignment</li>
                                <li>Receive Tea</li>           
                                <li>Release Tea</li>
                            </ul>
                        )}
                    </li>
                    <li onMouseEnter={() =>setCargoDropdownOpen(true)} onMouseLeave={()=>setCargoDropdownOpen(false)}>
                        Cargo
                        {cargoDropdownOpen && (
                            <ul className={styles.dropdown}>
                                <li>Receive Consignment</li>
                                <li>Release Cargo</li>
                            </ul>
                        )}
                    </li>
                    <li onMouseEnter={()=>setReportsDropdownOpen(true)} onMouseLeave={()=>setReportsDropdownOpen(false)}>
                        Reports
                        {reportsDropdownOpen && (
                            <ul className={styles.dropdown}>
                                <li>Tea Report</li>
                                <li>Cargo Report</li>
                            </ul>
                        )}

                    </li>
                    <li>Users</li>
                    <li>Settings</li>
                </ul>
            </aside>
            <main className={styles.content}>
                <section className={styles.card}>
                    <h2>Card Title</h2>
                    <p>This is a card section with some content.</p>
                </section>
                <section className={styles.data}>
                    <h2>Data Section</h2>
                    <p>Here you can display various data visualizations or tables.</p>
                </section>
                <section className={styles.card}>
                    <h2>Card Title</h2>
                    <p>This is a card section with some content.</p>
                </section>
                <section className={styles.data}>
                    <h2>Data Section</h2>
                    <p>Here you can display various data visualizations or tables.</p>
                </section>
                <section className={styles.card}>
                    <h2>Card Title</h2>
                    <p>This is a card section with some content.</p>
                </section>
                <section className={styles.data}>
                    <h2>Data Section</h2>
                    <p>Here you can display various data visualizations or tables.</p>
                </section>
                <section className={styles.data}>
                    
                </section>
            </main>
        </>
    );
}

export default Dashboard;