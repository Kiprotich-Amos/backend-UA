import React from "react";
import HomePage from "./index";
import styles from "@/app/utils/css/home/page.module.css";

const HomeDashPage = () =>{
    return(
        <div className={styles.body}>
            <HomePage />
        </div>
    );
};
export default HomeDashPage;
