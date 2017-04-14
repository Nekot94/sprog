
const gulp = require('gulp');
const pug = require('gulp-pug');

gulp.task('pages', function() {

    return gulp
	    .src('./source/pages/*.pug')
	    .pipe(pug({pretty: true}))
	    .pipe(gulp.dest('./public'));

});

gulp.task('watch', function() {

    gulp.watch('./source/**/*.pug', ['pages']);

});
