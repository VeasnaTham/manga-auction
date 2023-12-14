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
          value="Action"
          title="Action"
          name="test"
        />
        <Input
          handleChange={handleChange}
          value="Adventure"
          title="Adventure"
          name="test"
        />
        <Input
          handleChange={handleChange}
          value="Fantasy"
          title="Fantasy"
          name="test"
        />
        <Input
          handleChange={handleChange}
          value="Horror"
          title="Horror"
          name="test"
        />
        <Input
          handleChange={handleChange}
          value="Isekai"
          title="Isekai"
          name="test"
        />
        <Input
          handleChange={handleChange}
          value="Medical"
          title="Medical"
          name="test"
        />
        <Input
          handleChange={handleChange}
          value="Romance"
          title="Romance"
          name="test"
        />
        <Input
          handleChange={handleChange}
          value="Sci-Fi"
          title="Sci-Fi"
          name="test"
        />
        <Input
          handleChange={handleChange}
          value="Supernatural"
          title="Supernatural"
          name="test"
        />
        <Input
          handleChange={handleChange}
          value="Webtoons"
          title="Webtoons"
          name="test"
        />
      </div>
    </div>
  );
}


export default Genre;