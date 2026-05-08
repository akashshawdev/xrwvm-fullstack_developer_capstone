import React, { useState } from "react";
import "./Register.css";

const Register = ({ onClose }) => {
  const [userName, setUserName] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [error, setError] = useState("");

  const handleRegister = async (e) => {
    e.preventDefault();
    setError("");

    const response = await fetch("/djangoapp/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        userName,
        firstName,
        lastName,
        email,
        password,
      }),
    });

    const json = await response.json();
    if (json.status) {
      window.location.href = "/djangoapp/";
    } else {
      setError(json.error || "Registration failed. Please try again.");
    }
  };

  return (
    <div className="register-overlay">
      <div className="register-modal">
        <h2>Create Account</h2>
        {error && <p className="error-msg">{error}</p>}
        <form onSubmit={handleRegister}>
          <input
            type="text"
            placeholder="Username"
            value={userName}
            onChange={(e) => setUserName(e.target.value)}
            required
          />
          <input
            type="text"
            placeholder="First Name"
            value={firstName}
            onChange={(e) => setFirstName(e.target.value)}
            required
          />
          <input
            type="text"
            placeholder="Last Name"
            value={lastName}
            onChange={(e) => setLastName(e.target.value)}
            required
          />
          <input
            type="email"
            placeholder="Email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <button type="submit" className="register-btn">Register</button>
          <button type="button" className="close-btn" onClick={onClose}>Cancel</button>
        </form>
      </div>
    </div>
  );
};

export default Register;
