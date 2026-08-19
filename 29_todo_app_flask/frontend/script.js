const API_URL = "http://127.0.0.1:5050/todos";

const form = document.getElementById("todo-form");
const titleInput = document.getElementById("title");
const todoList = document.getElementById("todo-list");

const pendingCount = document.getElementById("pending-count");
const completedCount = document.getElementById("completed-count");

const filters = document.querySelectorAll(".filter");

let todos = [];
let currentFilter = "all";


// =========================
// GET TODOS
// =========================

async function getTodos(filter = "all") {

    try {

        let url = API_URL;

        // Add query parameter when filtering
        if (filter === "pending") {
            url = `${API_URL}?completed=false`;
        }

        if (filter === "completed") {
            url = `${API_URL}?completed=true`;
        }


        const response = await fetch(url);

        if (!response.ok) {
            throw new Error("Failed to fetch todos");
        }


        todos = await response.json();


        displayTodos();

    } catch (error) {

        console.error(error);

        todoList.innerHTML = `
            <div class="empty-state">
                <div class="empty-icon">⚠️</div>

                <h2>Unable to load todos</h2>

                <p>Make sure your Flask server is running.</p>
            </div>
        `;
    }
}


// =========================
// DISPLAY TODOS
// =========================

function displayTodos() {

    if (todos.length === 0) {

        todoList.innerHTML = `
            <div class="empty-state">
                <div class="empty-icon">✨</div>

                <h2>Your list is clear!</h2>

                <p>Add a task above to get started.</p>
            </div>
        `;

        return;
    }


    todoList.innerHTML = "";


    todos.forEach(todo => {

        const card = document.createElement("div");

        card.className = "todo-card";


        card.innerHTML = `
            <input
                type="checkbox"
                class="todo-checkbox"
                ${todo.completed ? "checked" : ""}
            >

            <span class="todo-title ${todo.completed ? "completed" : ""}">
                ${escapeHtml(todo.title)}
            </span>

            <div class="todo-actions">

                <button class="edit-btn">
                    Edit
                </button>

                <button class="delete-btn">
                    Delete
                </button>

            </div>
        `;


        // Checkbox
        const checkbox = card.querySelector(".todo-checkbox");

        checkbox.addEventListener("change", () => {
            toggleTodo(todo.id, checkbox.checked);
        });


        // Edit
        const editButton = card.querySelector(".edit-btn");

        editButton.addEventListener("click", () => {
            editTodo(todo.id, todo.title);
        });


        // Delete
        const deleteButton = card.querySelector(".delete-btn");

        deleteButton.addEventListener("click", () => {
            deleteTodo(todo.id);
        });


        todoList.appendChild(card);
    });
}


// =========================
// ADD TODO
// =========================

form.addEventListener("submit", async (event) => {

    event.preventDefault();

    const title = titleInput.value.trim();

    if (!title) {
        return;
    }


    try {

        const response = await fetch(API_URL, {

            method: "POST",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                title: title
            })
        });


        if (!response.ok) {
            throw new Error("Failed to create todo");
        }


        titleInput.value = "";

        // Refresh current filter
        await getTodos(currentFilter);

    } catch (error) {

        console.error(error);
    }
});


// =========================
// TOGGLE TODO
// =========================

async function toggleTodo(id, completed) {

    try {

        const response = await fetch(`${API_URL}/${id}`, {

            method: "PUT",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                completed: completed
            })
        });


        if (!response.ok) {
            throw new Error("Failed to update todo");
        }


        // Refresh current filter
        await getTodos(currentFilter);

    } catch (error) {

        console.error(error);
    }
}


// =========================
// EDIT TODO
// =========================

async function editTodo(id, currentTitle) {

    const newTitle = prompt(
        "Edit your task:",
        currentTitle
    );


    if (
        newTitle === null ||
        newTitle.trim() === ""
    ) {
        return;
    }


    try {

        const response = await fetch(`${API_URL}/${id}`, {

            method: "PUT",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                title: newTitle.trim()
            })
        });


        if (!response.ok) {
            throw new Error("Failed to update todo");
        }


        // Refresh current filter
        await getTodos(currentFilter);

    } catch (error) {

        console.error(error);
    }
}


// =========================
// DELETE TODO
// =========================

async function deleteTodo(id) {

    const confirmed = confirm(
        "Are you sure you want to delete this task?"
    );


    if (!confirmed) {
        return;
    }


    try {

        const response = await fetch(`${API_URL}/${id}`, {
            method: "DELETE"
        });


        if (!response.ok) {
            throw new Error("Failed to delete todo");
        }


        // Refresh current filter
        await getTodos(currentFilter);

    } catch (error) {

        console.error(error);
    }
}


// =========================
// FILTERS
// =========================

filters.forEach(button => {

    button.addEventListener("click", () => {

        // Remove active state
        filters.forEach(btn => {
            btn.classList.remove("active");
        });


        // Add active state
        button.classList.add("active");


        // Get selected filter
        currentFilter = button.dataset.filter;


        // Ask backend for filtered data
        getTodos(currentFilter);
    });
});


// =========================
// COUNTERS
// =========================

async function updateCounters() {

    try {

        const [pendingResponse, completedResponse] = await Promise.all([

            fetch(`${API_URL}?completed=false`),

            fetch(`${API_URL}?completed=true`)

        ]);


        const pendingTodos = await pendingResponse.json();
        const completedTodos = await completedResponse.json();


        pendingCount.textContent = pendingTodos.length;

        completedCount.textContent = completedTodos.length;

    } catch (error) {

        console.error(error);
    }
}


// =========================
// SECURITY HELPER
// =========================

function escapeHtml(text) {

    const div = document.createElement("div");

    div.textContent = text;

    return div.innerHTML;
}


// =========================
// INITIAL LOAD
// =========================

getTodos();

updateCounters();