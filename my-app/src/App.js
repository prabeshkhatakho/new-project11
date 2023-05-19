import logo from './logo.svg';
import './App.css';
import {BrowserRouter as Router,Routes,Route,Link} from "react-router-dom";


import Language from './components/language'
import Newdata from './components/newdata'
import Home from './components/home'




function App() {
  return (
    <>
    

      <Router>
        <Routes>
          <Route path={"/"} element={<Home />}></Route> 
          
          <Route path='/Newdata' element ={<Newdata />}></Route>
          <Route path='/Language' element ={<Language />}></Route>
          
          
        </Routes>
      </Router>
    </>
  
  );
}

export default App;
