const mongoose = require('mongoose');

const reviewSchema = new mongoose.Schema({
    id: Number,
    name: String,
    dealership: Number,
    review: String,
    purchase: Boolean,
    purchase_date: String,
    car_make: String,
    car_model: String,
    car_year: Number,
});

const Reviews = mongoose.model('Reviews', reviewSchema);

module.exports = Reviews;
