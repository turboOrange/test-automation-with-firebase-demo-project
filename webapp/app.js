const firebaseConfig = { projectId: "demo-project" };
const app = firebase.initializeApp(firebaseConfig);
const db = firebase.firestore();

db.useEmulator("localhost", 8080);

const btn = document.getElementById("addBtn");
const list = document.getElementById("items");

btn.addEventListener("click", async () => {
  await db.collection("items").add({ name: "Test Item" });
  loadItems();
});

async function loadItems() {
  const snap = await db.collection("items").get();
  list.innerHTML = "";
  snap.forEach(doc => {
    const li = document.createElement("li");
    li.textContent = doc.data().name;
    list.appendChild(li);
  });
}

loadItems();

