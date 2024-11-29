import './App.css';
import './components/header'
import Home from './components/paginas/home';
import Add from './components/paginas/add';
import { BrowserRouter, Routes, Route } from "react-router-dom";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/adicionar" element={<Add />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
