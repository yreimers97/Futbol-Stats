import City from "./City"
import { useOutletContext } from "react-router-dom"

function CitiesList() {
    const {cities} = useOutletContext()
    console.log(cities)
    const citiesComponents = cities.map(city => {
        return <City key={city.id} city={city}/>
    })
    return <ul>
                {citiesComponents}
        </ul>
}

export default CitiesList