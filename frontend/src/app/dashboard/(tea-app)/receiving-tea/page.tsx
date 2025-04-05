import React from "react";
import MyReusableTable from './index';
import styles from "@/app/utils/css/dash/indexReceive.module.css"


const ReceivePage = () =>{
    return(
        <div className={styles.body}>
            <MyReusableTable />
        </div>
    );
};
export default ReceivePage;