import Genre from './Genre/Genre'
import Price from './Price/Price'
import './Sidebar.css'

const Sidebar = ({ handleChange }) => {
    return (
      <>
        <section className="sidebar">
          <div className="logo-container">
            <h1>🛒</h1>
          </div>
          <Genre handleChange={handleChange} />
          <Price handleChange={handleChange} />
        </section>
      </>
    );
  };
export default Sidebar;