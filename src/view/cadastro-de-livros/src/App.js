import './App.css';
import './components/header'
import Header from './components/header/index.js';
import Add from './components/adicionadosRecentemente/index.js';

function App() {
  return (
    <div>
      <Header/>
      <div>
        <Add/>
      </div>
    </div>
    
  );
}

export default App;
