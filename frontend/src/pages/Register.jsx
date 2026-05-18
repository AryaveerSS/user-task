import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";

import api from "../services/api";

function Register() {
  const navigate = useNavigate();

  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: "",
  });

  const [error, setError] = useState("");

  const handleChange = (e) => {
    setFormData({
      ...formData,
      [e.target.name]: e.target.value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    setError("");

    try {
      await api.post(
        "/users/register",
        formData
      );

      navigate("/login");

    }
    catch (err) {

  console.log(err.response.data);

  if (
    err.response &&
    err.response.data
  ) {

    if (
      err.response.data.message
    ) {

      setError(
        err.response.data.message
      );

    }
    else if (
      Array.isArray(
        err.response.data.detail
      )
    ) {

      setError(
        err.response.data.detail[0].msg
      );

    }
    else {

      setError("Registration failed");

    }

  } else {

    setError("Registration failed");

  }

}
  };

  return (

  <div className="auth-container">

    <div className="auth-card">

      <h1>Create Account</h1>

      <form onSubmit={handleSubmit}>

        <input
          type="text"
          name="name"
          placeholder="Full Name"
          value={formData.name}
          onChange={handleChange}
          required
        />

        <input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
          required
        />

        <input
          type="password"
          name="password"
          placeholder="Password"
          value={formData.password}
          onChange={handleChange}
          required
        />

        {
          error && (
            <p className="error-message">
              {error}
            </p>
          )
        }

        <button type="submit">
          Register
        </button>

      </form>

      <div className="auth-link">

        <Link to="/login">
          Already have an account?
        </Link>

      </div>

    </div>

  </div>

);
}

export default Register;