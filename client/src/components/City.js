function City({city}) {
    console.log(city)
    return <li>
             <h1>city #{city.id}</h1>
             <h2>name: {city.name}</h2>
             <h2>country: {city.country}</h2>
             <h2>continent: {city.continent}</h2>
        </li>
}

export default City