import { useEffect, useState } from "react";

import api from "../services/api";

function AdminDashboard() {

  const [users, setUsers] =
    useState([]);

  const [tasks, setTasks] =
    useState([]);


  const fetchData = async () => {

    try {

      const usersResponse =
        await api.get(
          "/admin/users"
        );

      const tasksResponse =
        await api.get(
          "/admin/tasks"
        );

      setUsers(
        usersResponse.data
      );

      setTasks(
        tasksResponse.data
      );

    } catch (err) {

      console.log(err);

    }

  };


  useEffect(() => {

    fetchData();

  }, []);


  const handleDeleteUser =
    async (userId) => {

      try {

        await api.delete(
          `/admin/users/${userId}`
        );

        fetchData();

      } catch (err) {

        console.log(err);

      }

    };


  const handleDeleteTask =
    async (taskId) => {

      try {

        await api.delete(
          `/admin/tasks/${taskId}`
        );

        fetchData();

      } catch (err) {

        console.log(err);

      }

    };


  return (

    <div
      style={{
        maxWidth: "900px",
        margin: "40px auto",
      }}
    >

      <h1>Admin Dashboard</h1>

      <hr />

      <h2>All Users</h2>

      {
        users.map((user) => (

          <div
            key={user.id}
            style={{
              border: "1px solid gray",
              padding: "10px",
              marginBottom: "10px",
            }}
          >

            <p>
              {user.name}
            </p>

            <p>
              {user.email}
            </p>

            <p>
              {user.role}
            </p>

            <button
              onClick={() =>
                handleDeleteUser(
                  user.id
                )
              }
            >
              Delete User
            </button>

          </div>

        ))
      }


      <hr />

      <h2>All Tasks</h2>

      {
        tasks.map((task) => (

          <div
            key={task.id}
            style={{
              border: "1px solid gray",
              padding: "10px",
              marginBottom: "10px",
            }}
          >

            <p>
              {task.title}
            </p>

            <p>
              {task.description}
            </p>

            <button
              onClick={() =>
                handleDeleteTask(
                  task.id
                )
              }
            >
              Delete Task
            </button>

          </div>

        ))
      }

    </div>

  );

}

export default AdminDashboard;