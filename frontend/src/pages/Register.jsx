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
    <div
      style={{
        maxWidth: "400px",
        margin: "100px auto",
      }}
    >
      <h2>Register</h2>

      <form onSubmit={handleSubmit}>

        <input
          type="text"
          name="name"
          placeholder="Name"
          value={formData.name}
          onChange={handleChange}
          required
        />

        <br /><br />

        <input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
          required
        />

        <br /><br />

        <input
          type="password"
          name="password"
          placeholder="Password"
          value={formData.password}
          onChange={handleChange}
          required
        />

        <br /><br />

        <button type="submit">
          Register
        </button>

      </form>

      <br />

      {
  error && (
    <p
      style={{
        color: "red",
        marginTop: "10px",
      }}
    >
      {error}
    </p>
  )
}
      <Link to="/login">
        Already have an account?
      </Link>
    </div>
  );
}

export default Register;