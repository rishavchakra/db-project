/** Helper types **/

// Country ID, like the keys in the SQL table
type countryID = number;

// Map from a country's countryID to its name
// to be populated with successive queries
type countryIDName = {
  // Mappable type: mapping from countryID to string
  [id: countryID]: string,
};

// For use with the first question:
// How do countries' happiness affect their suicide rates?
// i.e. is happiness an effective heuristic/predictor for suicide rate?
type countrySuicidesHappiness = {
  country: countryID,
  happinessScore: number,
  suicides: number,
};

// For use with the third question:
// Are there any countries where the suicide rate is a significant factor in life expectancy?
type countrySuicidesLifeExpectancy = {
  country: countryID,
  lifeExpectancy: number,
  suicides: number,
};

// For use with the fourth question:
// Where is substance abuse more affected by age, and where is it more 
type countrySuicidesAgeGender = {
  country: countryID,
}

export {
  type countryID,
  type countryIDName,
  type countrySuicidesHappiness,
  type countrySuicidesLifeExpectancy,
  type countrySuicidesAgeGender,
}
