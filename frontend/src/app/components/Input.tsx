import React, {ChangeEvent} from 'react';
import styles from '@/app/components/css/Input.module.css';

interface InputProps{
    type?: 'text'| 'password'| 'email' | 'number'| 'date' |'tel' |'step';
    id?: string;
    step?:string;
    name?: string;
    placeholder?: string;
    value?:string | number;
    onChange?: (event:ChangeEvent<HTMLInputElement>) => void;
} 
const Input: React.FC<InputProps> = ({
    type = "text",
    step,
    id,
    name,
    placeholder,
    value,
    onChange
}) =>{
    return(
        <div className={styles.inputWrapper}>
            <input type={type}
            id={id}
            step={step}
            name={name}
            placeholder={placeholder}
            value={value}
            onChange={onChange}
            className={styles.inputField}/>
        </div>
    );
};
export default Input