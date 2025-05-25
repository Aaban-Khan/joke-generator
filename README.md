<h1 align="center">Random Joke Generator (Terminal-Based)</h1>

<p align="center">
  <strong>A fun and interactive Python terminal application that fetches random jokes from an online API and saves them locally with timestamps!</strong>
</p>

---

<h2>🚀 Features</h2>

<ul>
  <li>🎭 Fetches random jokes from <a href="https://jokeapi.dev">JokeAPI</a>.</li>
  <li>💾 Automatically stores jokes with timestamps in a structured <code>database/</code> folder.</li>
  <li>⌛ Typewriter effect for better terminal user experience.</li>
  <li>📁 Creates daily log files for joke sessions in <code>.txt</code> format.</li>
  <li>🎨 Uses color formatting (via <code>colorama</code>) for improved readability.</li>
</ul>

---

<h2>🛠️ Technologies Used</h2>

<ul>
  <li><strong>Python:</strong> Core logic and scripting</li>
  <li><strong>Colorama:</strong> Terminal text coloring</li>
  <li><strong>Requests:</strong> Fetching jokes from the JokeAPI</li>
  <li><strong>Datetime & OS:</strong> File handling and timestamping</li>
</ul>

---

<h2>📦 Folder Structure</h2>

<pre>
/main.py                 -> Main script for running the joke generator
/requirements.txt        -> Required dependencies
/database/               -> Automatically created to store jokes by date
  ├── quotes_MMM-DD-YYYY.txt -> Saved jokes for the session (auto-named by date)
</pre>

---

<h2>⚙️ How to Use</h2>

<ol>
  <li>Clone the repository:</li>
  <pre>git clone https://github.com/your-username/random-joke-generator.git</pre>

  <li>Install the dependencies:</li>
  <pre>pip install -r requirements.txt</pre>

  <li>Run the script:</li>
  <pre>python main.py</pre>

  <li>Enjoy fresh jokes and check <code>database/</code> folder for saved logs!</li>
</ol>

---

<h2>🎯 How It Works</h2>

<ul>
  <li>Launches with a typewriter-style welcome message.</li>
  <li>On each <code>y</code> input, fetches a new joke and appends it to a dated file.</li>
  <li>Uses timestamps to track when each joke was fetched.</li>
  <li>Gracefully exits and shows total jokes generated when the user types <code>n</code>.</li>
</ul>

---

<h2>🗂️ Example Output in <code>database/</code> File</h2>

<pre>
# Saving Data....

1) Why did the chicken cross the road? To get to the other side! At 03:45:02 PM

2) I told my computer I needed a break, and now it won’t stop sending me KitKat ads. At 03:47:01 PM
</pre>

---

<h2>📜 License</h2>

<p>This project is licensed under the <strong>MIT License</strong> — free to use, modify, and distribute.</p>
