import React from 'react';
import LoginForm from '@/app/(auth)/login/index';
import styles from '@/app/utils/css/auth/login.module.css'

const LoginPage = () => {
  return (
    <div className={styles.container}>
      <LoginForm />
    </div>
  );
};export default LoginPage;