import React, { MouseEventHandler } from "react";
import styles from './css/Button.module.css';

interface ButtonProps{
    type?:'button' | 'submit' | 'reset';
    onClick?: MouseEventHandler<HTMLButtonElement>;
    id?:string;
    children?: React.ReactNode;
    className?: string;
    disabled?: boolean;
}

const Button: React.FC<ButtonProps> = ({
    type = 'button',
    id,
    onClick,
    children,
    className,
    disabled,

}) => {
    return(
        <button 
        type={type}
        id ={id}
        onClick={onClick}
        className={`${styles.button} ${className || ''}`}
        disabled={disabled}>
            {children}
        </button>
    );
};

export default Button;
