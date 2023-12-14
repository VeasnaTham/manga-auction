import './Recommended.css';


function Recommended() {
  return <>
    <div>
      <h2 className='recommended-title'>Recommended</h2>
      <div className="recommended-flex">
          <button className='btns'>All</button>
          <button className='btns'>Manga</button>
          <button className='btns'>Manhwa</button>
          <button className='btns'>Manhua</button>
      </div>
    </div>
  </>
}

export default Recommended;