import React from "react";
import styles from '@/app/components/css/Card.module.css'

interface CardProps{
    title?: string;
    children: React.ReactNode;
    actions?: React.ReactNode;
}

const Card: React.FC<CardProps> =({title, children, actions}) =>{
    return(
        <div className={styles.card}>
            {title && (
                <div className={styles.cardHeader}>
                    <h3>{title}</h3>
                </div>
            )}
            <div className={styles.cardBody}>
                {children}
            </div>
            {actions &&(
                <div className={styles.carFooter}>
                    {actions}
                </div>
            )}
        </div>
    );
};
export default Card;