async function generatePlan() {
    let branch = document.getElementById("branch").value;
    let goal = document.getElementById("goal").value;
    let hours = document.getElementById("hours").value;

    let response = await fetch("http://127.0.0.1:5000/plan", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ branch, goal, hours })
    });

    let data = await response.json();
    document.getElementById("output").innerText = data.plan;
}