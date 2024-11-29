import React from "react";
import './style.css';
import search from "../../assets/search.png"
import { Link } from "react-router-dom";

const Header = () => {
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
                    value={''}
                    onChange={''}
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