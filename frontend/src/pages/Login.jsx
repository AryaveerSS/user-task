import { useState } from "react";
import { useNavigate, Link } from "react-router-dom";
import { useContext } from "react";

import api from "../services/api";

import { AuthContext } from "../context/AuthContext";

function Login() {
  const navigate = useNavigate();

  const { login } = useContext(AuthContext);

  const [formData, setFormData] = useState({
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
      const response = await api.post(
        "/users/login",
        formData
      );

      login(
        response.data.access_token
      );
        localStorage.setItem(
        "role",
        response.data.user.role
        );

      navigate("/");

    } catch (err) {

  console.log(
  err.response?.data
  )

  if (
  err.response?.data
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
    else if (
      err.response.data.detail
    ) {

      setError(
        err.response.data.detail
      );

    }
    else {

      setError("Login failed");

    }

  } else {

    setError("Login failed");

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
      <h2>Login</h2>

      <form onSubmit={handleSubmit}>

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
          Login
        </button>

      </form>

      <br />

      {error && (
  <p
    style={{
      color: "red",
      marginTop: "10px",
    }}
  >
    {error}
  </p>
)}

      <Link to="/register">
        Create new account
      </Link>
    </div>
  );
}

export default Login;   