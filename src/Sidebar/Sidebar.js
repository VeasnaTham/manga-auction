import Genre from './Genre/Genre'
import Price from './Price/Price'
import './Sidebar.css'

function Sidebar() {
  return <>
    <section className="sidebar">
        <div className="logo-container">
            <h1>🛒</h1>
        </div>
        <Genre/>
        <Price/>
        
    </section>
  </>
}
export default Sidebar;