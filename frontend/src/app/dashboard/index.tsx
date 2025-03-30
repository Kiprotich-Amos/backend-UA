import React from "react";
import styles from '@/app/utils/css/dash/dashboard.module.css';

interface DashboardProps{};

const Dashboard : React.FC<DashboardProps> = () =>{
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
                <h3>Menu</h3>
                <ul>
                    <li>Dashboard</li>
                    <li>Reports</li>
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
            </main>
        </>
    );
}

export default Dashboard;