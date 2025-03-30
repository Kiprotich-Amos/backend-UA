"use client";
import { useRouter } from "next/navigation";
import React, { useState, ChangeEvent, FormEvent } from "react";
import Input from "@/app/components/Input";
import Button from "@/app/components/Button";
import styles from "@/app/utils/css/auth/RegistrationForm.module.css";

interface RegistrationFormProps{};

const RegistrationForm: React.FC < RegistrationFormProps > = () =>{
    const [firstName, setFirstName] = useState<string>('');
    const [lastName, setLastName] = useState<string>('');
    const[mobile, setMobile] = useState<string>('');
    const [email, setEmail] = useState<string>('');
    const [password, setPassword] = useState<string>('');
    const [password2, setPassword2] = useState<string>('');
    const router = useRouter();

    const handleFirstNameChange = (e: ChangeEvent<HTMLInputElement>) => {
        setFirstName(e.target.value);
    };

    const handleLastNameChange = (e: ChangeEvent<HTMLInputElement>) => {
        setLastName(e.target.value);
    };

    const handleMobileChange = (e: ChangeEvent<HTMLInputElement>) => {
        setMobile(e.target.value);
    };

    const handleEmailChange = (e: ChangeEvent<HTMLInputElement>) => {
        setEmail(e.target.value);
    };

    const handlePasswordChange = (e: ChangeEvent<HTMLInputElement>) => {
        setPassword(e.target.value);
    };

    const handlePassword2Change = (e: ChangeEvent<HTMLInputElement>) => {
        setPassword2(e.target.value);
    };

    const handleSubmit = (e: FormEvent) => {
        e.preventDefault();
        if (password !== password2) {
            alert("Passwords do not match!");
            return;
        }
        console.log('Registration submitted:', { firstName, lastName, mobile, email, password });
        // you would send this data to your Django backend
        // to create the user.
        router.push('/login'); 
    };

    return(
        <div className={styles.registrationContainer}> 
            <h2>Sign Up</h2>
            <form onSubmit={handleSubmit}>
                <Input
                    type="text"
                    id="firstName"
                    name="firstName"
                    placeholder="First Name"
                    value={firstName}
                    onChange={handleFirstNameChange}
                />
                <Input
                    type="text"
                    id="lastName"
                    name="lastName"
                    placeholder="Last Name"
                    value={lastName}
                    onChange={handleLastNameChange}
                />
                <Input
                    type="tel"
                    id="mobile"
                    name="mobile"
                    placeholder="Mobile Number"
                    value={mobile}
                    onChange={handleMobileChange}
                />
                <Input
                    type="email"
                    id="email"
                    name="email"
                    placeholder="Email Address"
                    value={email}
                    onChange={handleEmailChange}
                />
                <Input
                    type="password"
                    id="password"
                    name="password"
                    placeholder="Password"
                    value={password}
                    onChange={handlePasswordChange}
                />
                <Input
                    type="password"
                    id="password2"
                    name="password2"
                    placeholder="Confirm Password"
                    value={password2}
                    onChange={handlePassword2Change}
                />
                <Button type="submit">Register</Button>
            </form>
            <p>
                Already have an account? <a href="/auth/login">Log In</a>
            </p>
        </div>
    );
};
export default RegistrationForm;