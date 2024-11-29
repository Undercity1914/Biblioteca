import React from "react";
import './style.css';
import search from "../../assets/search.png"

const Header = () => {
    return (
        <nav class="header">
            <div class="header-title">
                <p>Minha</p>
                <p>Bilioteca</p>
                <p>Pessoal</p>
            </div>
            <div class="header-bar">
                <p class="header-text-bar" style={{marginLeft: "115px", cursor: "default"}}>
                    Procurar
                </p>
                <img src={search} alt="Search" style={{width: "15px", marginLeft: "10px", cursor: "pointer"}}/>
                <input
                    type="text"
                    value={''}
                    onChange={''}
                    class="header-search-bar"
                />
                <p class="header-text-bar" style={{marginLeft: "50px", cursor: "pointer"}}>
                    Adicionar
                </p>
                <p class="header-text-bar" style={{marginLeft: "50px", cursor: "pointer"}}>
                    Remover
                </p>
                <p class="header-text-bar" style={{marginLeft: "50px", cursor: "pointer"}}>
                    Editar
                </p>
                <p class="header-text-bar" style={{marginLeft: "50px", cursor: "pointer"}}>
                    Outros
                </p>
            </div>
        </nav>
    );
}

export default Header;