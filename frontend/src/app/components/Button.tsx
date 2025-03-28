import React, { MouseEventHandler } from "react";
import styles from './Button.module.css';

interface ButtonProps{
    type?:'button' | 'submit' | 'reset';
    onClick?: MouseEventHandler<HTMLButtonElement>;
    children?: React.ReactNode;
    disabled?: boolean;
}

const Button: React.FC<ButtonProps> = ({
    type = 'button',
    onClick,
    children,
    disabled,
}) => {
    return(
        <button 
        type={type}
        onClick={onClick}
        className={styles.button}
        disabled={disabled}>
            {children}
        </button>
    );
};

export default Button;
