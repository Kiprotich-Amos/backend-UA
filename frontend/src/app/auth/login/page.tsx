import React, { useState, ChangeEvent, FormEvent } from "react";
import Input from "@/app/components/Input";
import Button from "@/app/components/Button";
import styles from "util";

interface LoginFormProps {} // You might have props for the LoginForm later

const LoginForm: React.FC<LoginFormProps> = () =>{
    const [email, setEmail] = useState<string>('');
    const [password, setPassword] = useState<string>('');

    const handleEmailChange = (e:ChangeEvent<HTMLInputElement>) =>{
        setEmail(e.target.value);
    };
    const handlePasswordChange = (e: ChangeEvent<HTMLInputElement>) =>{
        setPassword(e.target.value);
    };
    const  handleSubmit =(e:FormEvent) =>{
        e.preventDefault();
        console.log('Login submitted: ', {email, password});
    };

    return(
        <div className={styles.loginContainer}>
            <h2>Login</h2>
            <form onSubmit={handleSubmit}>
                <Input type="email" id='email' name="email" placeholder="Email" value={email} onChange={handleEmailChange}/>
                <Input type="password" id = "password" name="password" placeholder="Password" value={password} onChange={handlePasswordChange}/>
                <Button type="submit">Login</Button>
            </form>
            <p>
                Don't have an  account? <a href="/auth/sign-up">Sign Up</a>
            </p>
        </div>
    );
};

export default LoginForm;
