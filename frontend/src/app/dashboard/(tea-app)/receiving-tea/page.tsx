import React from "react";
import TeaReceiving from './index';
import styles from "@/app/utils/css/dash/indexReceive.module.css"


const ReceiveTea = () =>{
    return(
        <div className={styles.body}>
            <TeaReceiving/>
        </div>
    );
};
export default ReceiveTea;
