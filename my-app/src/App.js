import logo from './logo.svg';
import './App.css';
import {BrowserRouter as Router,Routes,Route,Link} from "react-router-dom";
import Mardi from './components/mardi'
import Washingmachine from './components/washingmachine'
import Language from './components/language'
import Home from './components/home'
import Newfile from './components/newfile'
import Stories from './components/stories'
import Jsondata from './components/jsondata'

function App() {
  return (
    <Router>
      <Routes>
        <Route path={"/"} element={<jsondata />}></Route> 
        <Route path={"/Mardi"} element={<Mardi />}></Route> 
        <Route path='/Washingmachine' element ={<Washingmachine />}></Route>
        <Route path='/Language' element ={<Language />}></Route>
        <Route path='/Newfile' element={<Newfile />}></Route>
        <Route path='/Stories' element={<Stories />}></Route>
        <Route path='/Jsondata' element={<Jsondata />}></Route>
      </Routes>
    </Router>
  
  );
}

export default App;
