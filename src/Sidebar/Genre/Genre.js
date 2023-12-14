import './Genre.css';
function Genre() {
  return <div>
    <h2 className="sidebar-title">Genre</h2>
    <div>
      <label className="sidebar-label-container">
        <input type="radio" name='test'/>
        <span className='checkmark'></span>All
      </label>
    </div>
  </div>
  
}

export default Genre;