const API_URL = "http://127.0.0.1:5050/todos";

const form = document.getElementById("todo-form");
const titleInput = document.getElementById("title");
const todoList = document.getElementById("todo-list");

const pendingCount = document.getElementById("pending-count");
const completedCount = document.getElementById("completed-count");

const filters = document.querySelectorAll(".filter");

let todos = [];
let currentFilter = "all";

console.log("--LOADED--")


// =========================
// GET TODOS
// =========================

async function getTodos() {

    try {

        const response = await fetch(API_URL);

        if (!response.ok) {
            throw new Error("Failed to fetch todos");
        }

        todos = await response.json();

        updateCounters();
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

    let filteredTodos = todos;

    if (currentFilter === "pending") {
        filteredTodos = todos.filter(todo => !todo.completed);
    }

    if (currentFilter === "completed") {
        filteredTodos = todos.filter(todo => todo.completed);
    }


    if (filteredTodos.length === 0) {

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

    filteredTodos.forEach(todo => {

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

        await getTodos();

    } catch (error) {
        console.error(error);
    }
});


// =========================
// TOGGLE TODO
// =========================

async function toggleTodo(id, completed) {

    try {

        await fetch(`${API_URL}/${id}`, {

            method: "PUT",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                completed: completed
            })
        });

        await getTodos();

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

        await fetch(`${API_URL}/${id}`, {

            method: "PUT",

            headers: {
                "Content-Type": "application/json"
            },

            body: JSON.stringify({
                title: newTitle.trim()
            })
        });

        await getTodos();

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

        await fetch(`${API_URL}/${id}`, {
            method: "DELETE"
        });

        await getTodos();

    } catch (error) {
        console.error(error);
    }
}


// =========================
// FILTERS
// =========================

filters.forEach(button => {

    button.addEventListener("click", () => {

        filters.forEach(btn => {
            btn.classList.remove("active");
        });

        button.classList.add("active");

        currentFilter = button.dataset.filter;

        displayTodos();
    });
});


// =========================
// COUNTERS
// =========================

function updateCounters() {

    const pending = todos.filter(
        todo => !todo.completed
    ).length;

    const completed = todos.filter(
        todo => todo.completed
    ).length;


    pendingCount.textContent = pending;

    completedCount.textContent = completed;
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