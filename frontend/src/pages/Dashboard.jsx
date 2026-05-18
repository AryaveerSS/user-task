import { useEffect, useState } from "react";

import api from "../services/api";

function Dashboard() {

  const [tasks, setTasks] = useState([]);

  const [title, setTitle] = useState("");

  const [description, setDescription] =
    useState("");

  const [createError, setCreateError] =
    useState("");

  const [updateError, setUpdateError] =
    useState("");

  const [editingTaskId, setEditingTaskId] =
    useState(null);

  const [editTitle, setEditTitle] =
    useState("");

  const [editDescription, setEditDescription] =
    useState("");


  const fetchTasks = async () => {

    try {

      const response = await api.get(
        "/tasks"
      );

      setTasks(response.data);

    } catch (err) {

      console.log(err);

    }

  };


  useEffect(() => {

    fetchTasks();

  }, []);


  const handleCreateTask = async (e) => {

    e.preventDefault();

    setCreateError("");

    try {

      await api.post(
        "/tasks",
        {
          title,
          description,
        }
      );

      setTitle("");

      setDescription("");

      fetchTasks();

    } catch (err) {

      console.log(err.response.data);

      if (
        err.response &&
        err.response.data
      ) {

        if (
          err.response.data.message
        ) {

          setCreateError(
            err.response.data.message
          );

        }
        else if (
          Array.isArray(
            err.response.data.detail
          )
        ) {

          setCreateError(
            err.response.data.detail[0].msg
          );

        }
        else {

          setCreateError(
            "Task creation failed"
          );

        }

      } else {

        setCreateError(
          "Task creation failed"
        );

      }

    }

  };


  const handleDeleteTask = async (
    taskId
  ) => {

    try {

      await api.delete(
        `/tasks/${taskId}`
      );

      fetchTasks();

    } catch (err) {

      console.log(err);

    }

  };


  const handleToggleComplete = async (
    task
  ) => {

    try {

      await api.put(
        `/tasks/${task.id}`,
        {
          completed: !task.completed,
        }
      );

      fetchTasks();

    } catch (err) {

      console.log(err);

    }

  };


  const handleEditClick = (task) => {

    setUpdateError("");

    setEditingTaskId(task.id);

    setEditTitle(task.title);

    setEditDescription(
      task.description || ""
    );

  };


  const handleUpdateTask = async (
    taskId
  ) => {

    setUpdateError("");

    try {

      await api.put(
        `/tasks/${taskId}`,
        {
          title: editTitle,
          description: editDescription,
        }
      );

      setEditingTaskId(null);

      fetchTasks();

    } catch (err) {

      console.log(err.response.data);

      if (
        err.response &&
        err.response.data
      ) {

        if (
          err.response.data.message
        ) {

          setUpdateError(
            err.response.data.message
          );

        }
        else if (
          Array.isArray(
            err.response.data.detail
          )
        ) {

          setUpdateError(
            err.response.data.detail[0].msg
          );

        }
        else {

          setUpdateError(
            "Task update failed"
          );

        }

      } else {

        setUpdateError(
          "Task update failed"
        );

      }

    }

  };


  const handleLogout = () => {

    localStorage.removeItem("token");

    window.location.href = "/login";

  };


  return (

    <div
      style={{
        maxWidth: "700px",
        margin: "40px auto",
      }}
    >

      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
        }}
      >

        <h1>Dashboard</h1>

        <button onClick={handleLogout}>
          Logout
        </button>

      </div>


      <form onSubmit={handleCreateTask}>

        <input
          type="text"
          placeholder="Task title"
          value={title}
          onChange={(e) =>
            setTitle(e.target.value)
          }
          required
        />

        <br /><br />

        <textarea
          placeholder="Description"
          value={description}
          onChange={(e) =>
            setDescription(e.target.value)
          }
        />

        <br /><br />

        <button type="submit">
          Create Task
        </button>

      </form>


      {
        createError && (
          <p
            style={{
              color: "red",
              marginTop: "10px",
            }}
          >
            {createError}
          </p>
        )
      }


      <hr />

      <h2>Your Tasks</h2>


      {
        tasks.length === 0 ? (

          <p>No tasks found</p>

        ) : (

          tasks.map((task) => (

            <div
              key={task.id}
              style={{
                border: "1px solid gray",
                padding: "15px",
                marginBottom: "10px",
              }}
            >

              {
                editingTaskId === task.id ? (

                  <div>

                    <input
                      type="text"
                      value={editTitle}
                      onChange={(e) =>
                        setEditTitle(
                          e.target.value
                        )
                      }
                    />

                    <br /><br />

                    <textarea
                      value={editDescription}
                      onChange={(e) =>
                        setEditDescription(
                          e.target.value
                        )
                      }
                    />

                    <br /><br />

                    <button
                      onClick={() =>
                        handleUpdateTask(
                          task.id
                        )
                      }
                    >
                      Save
                    </button>


                    {
                      updateError && (
                        <p
                          style={{
                            color: "red",
                            marginTop: "10px",
                          }}
                        >
                          {updateError}
                        </p>
                      )
                    }

                  </div>

                ) : (

                  <div>

                    <h3>
                      {task.title}
                    </h3>

                    <p>
                      {task.description}
                    </p>

                    <p>
                      Status:
                      {" "}
                      {
                        task.completed
                          ? "Completed"
                          : "Pending"
                      }
                    </p>

                    <button
                      onClick={() =>
                        handleToggleComplete(
                          task
                        )
                      }
                    >
                      Toggle Status
                    </button>

                    <button
                      onClick={() =>
                        handleEditClick(
                          task
                        )
                      }
                      style={{
                        marginLeft: "10px",
                      }}
                    >
                      Edit
                    </button>

                    <button
                      onClick={() =>
                        handleDeleteTask(
                          task.id
                        )
                      }
                      style={{
                        marginLeft: "10px",
                      }}
                    >
                      Delete
                    </button>

                  </div>

                )
              }

            </div>

          ))

        )
      }

    </div>

  );

}

export default Dashboard;