export default function Login(){
    const mail = "Enter Your Email";
    const pass = "Enter  Your password";
    return(
        <div>
            <form>
                <label htmlFor=""> E-mail</label>
                <input type="Email" value={mail}></input>
                <label>Password</label>
                <input type="Password" value={pass}></input>
                <input type="Submit"></input>
            </form>
        </div>
    );
}