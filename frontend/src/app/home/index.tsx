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
          <p>View and manage storage in our warehouse.</p>
        </Card>

        <Card title="C & F" href="/clearing-and-forwarding">
          <p>Handle clearing and forwarding operations.</p>
        </Card>

        <Card title="Administration" href="/admin">
          <p>Access administrative tools and settings.</p>
        </Card>
        <Card title="Producer" href="/admin">
          <p>Access Producer Services in our warehouse.</p>
        </Card>
        <Card title="Broker" href="/admin">
          <p>Access Broker Services in our warehouse.</p>
        </Card>
      </div>
    </div>
  );
};

export default HomePage;