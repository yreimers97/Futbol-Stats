import React, { useEffect, useState } from "react";
import { Outlet } from "react-router-dom";

function App() {
  const [cities, setCities] = useState([])

  useEffect(() => {
  fetch('/cities')
  .then(response => response.json())
  .then(citiesData => setCities(citiesData))
  }, [])

  return <div>
            <Outlet context={{cities: cities}}/>
        </div>
}

export default App;
