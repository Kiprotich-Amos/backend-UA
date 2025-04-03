import React from 'react';
import Card from '@/app/components/card'
import styles from "@/app/utils/css/home/home.module.css"

const HomePage: React.FC = () => {
  return (
    <div className={styles.container}>
      <h1 className={styles.title}>Welcome to Our Platform</h1>
      <div className={styles.cardGrid}>
        <Card title="Accounts" href="/accounts">
          <p>Manage your financial accounts here.</p>
        </Card>

        <Card title="Warehouse" href="/warehouse">
          <p>View and manage inventory in our warehouse.</p>
        </Card>

        <Card title="C & F" href="/clearing-and-forwarding">
          <p>Handle clearing and forwarding operations.</p>
        </Card>

        <Card title="Administration" href="/admin">
          <p>Access administrative tools and settings.</p>
        </Card>
      </div>
    </div>
  );
};

export default HomePage;