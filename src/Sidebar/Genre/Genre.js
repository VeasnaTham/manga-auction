import Input from '../../components/Input';
import './Genre.css';
function Genre({ handleChange }) {
  return (
    <div>
      <h2 className="sidebar-title">Genre</h2>

      <div>
        <label className="sidebar-label-container">
          <input onChange={handleChange} type="radio" value="" name="test" />
          <span className="checkmark"></span>All
        </label>
        <Input
          handleChange={handleChange}
          value="action"
          title="Action"
          name="test"
        />
        <Input
          handleChange={handleChange}
          value="adventure"
          title="Adventure"
          name="test"
        />
        <Input
          handleChange={handleChange}
          value="fantasy"
          title="Fantasy"
          name="test"
        />
        <Input
          handleChange={handleChange}
          value="horror"
          title="Horror"
          name="test"
        />
        <Input
          handleChange={handleChange}
          value="isekai"
          title="Isekai"
          name="test"
        />
        <Input
          handleChange={handleChange}
          value="medical"
          title="Medical"
          name="test"
        />
        <Input
          handleChange={handleChange}
          value="romance"
          title="Romance"
          name="test"
        />
        <Input
          handleChange={handleChange}
          value="sci-fi"
          title="Sci-Fi"
          name="test"
        />
        <Input
          handleChange={handleChange}
          value="supernatural"
          title="Supernatural"
          name="test"
        />
        <Input
          handleChange={handleChange}
          value="webtoons"
          title="Webtoons"
          name="test"
        />
      </div>
    </div>
  );
}


export default Genre;