import React, {useEffect, useState} from "react";
import './style.css';
import search from "../../assets/search.png"
import { Link } from "react-router-dom";

const Header = () => {
    const [searchQueue, setSearchQueue] = useState('');
    const [resultQueue, setResultQueue] = useState([]);

    const fetchResults = async () => {
        if(!searchQueue) 
            return;

        try{
            const response = await fetch(`http://locahost:8000/search?book=${searchQueue}`, {
                method: 'GET',
            });

            if (response.ok) {
                const data = await response.json();
                setResultQueue(data);
            }
            else {
                console.error("ERROR 404. NOT FOUND!")
            }
        }
        catch (error) {
            console.error(error)
        }
    }
    return (
        <nav class="header">
            <div class="header-title">
                <p>Minha</p>
                <p>Bilioteca</p>
                <p>Pessoal</p>
            </div>
            <div class="header-bar">
                <p class="header-text-bar" style={{marginLeft: "115px", cursor: "default", marginTop: "15px"}}>
                    Procurar
                </p>
                <img src={search} alt="Search" style={{width: "15px", marginLeft: "10px", cursor: "pointer"}}/>
                <input
                    type="text"
                    value={searchQueue}
                    onChange={(e) => setSearchQueue(e.target.value)}
                    class="header-search-bar"
                />
                <Link to="/adicionar" class="header-text-bar" style={{marginLeft: "50px", cursor: "pointer", textDecoration: "none", marginTop: "-5px"}}>
                    Adicionar
                </Link>
                <Link to="/remover" class="header-text-bar" style={{marginLeft: "50px", cursor: "pointer", textDecoration: "none", marginTop: "-5px"}}>
                    Remover
                </Link>
                <Link to="/editar" class="header-text-bar" style={{marginLeft: "50px", cursor: "pointer", textDecoration: "none", marginTop: "-5px"}}>
                    Editar
                </Link>
                <p class="header-text-bar" style={{marginLeft: "50px", cursor: "pointer", marginTop: "15px"}}>
                    Outros
                </p>
            </div>
        </nav>
    );
}

export default Header;