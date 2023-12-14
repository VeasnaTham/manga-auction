const Card = ({ img, title, price }) => {
  return (
    <>
      <section className="card">
        <img src={img} alt={title} className="card-img" />
        <div className="card-details">
          <h3 className="card-title">{title}</h3>
          <section className="card-price">
            <div className="price">
              {price}
            </div>
          </section>
        </div>
      </section>
    </>
  );
};

export default Card;