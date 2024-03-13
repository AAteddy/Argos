import { useState, useEffect } from "react";

const App = () => {
  useEffect(() => {
    fetch("http://localhost:5000/server/hello")
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setMessage(data.message);
      })
      .catch((err) => console.log(err));
  }, []);

  const [message, setMessage] = useState("");

  return (
    <div className="container">
      <h1>{message}</h1>
    </div>
  );
};

export default App;
