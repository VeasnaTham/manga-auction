import Button from "../components/Buttons";
import "./Recommended.css";

const Recommended = ({ handleClick }) => {
  return (
    <>
      <div>
        <h2 className="recommended-title">Manga Category</h2>
        <div className="recommended-flex">
          <Button onClickHandler={handleClick} value="" title="All" />
          <Button onClickHandler={handleClick} value="Manga" title="Manga" />
          <Button onClickHandler={handleClick} value="Manhwa" title="Manhwa" />
          <Button onClickHandler={handleClick} value="Manhua" title="Manhua" />
        </div>
      </div>
    </>
  );
};

export default Recommended;