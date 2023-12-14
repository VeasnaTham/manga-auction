import Navigation from './Navigation/Nav';
import Books from './Books/Books';
import Recommended from './Recommended/Recommended';
import Sidebar from './Sidebar/Sidebar';


function App() {
  return (
    <>
      <Sidebar/>
      <Navigation/>
      <Recommended/>
      <Books/>
    </>
  );
}

export default App;
