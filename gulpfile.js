var gulp = require('gulp'),
    rename = require('gulp-rename'),
    prefix = require('gulp-autoprefixer'),
    minifycss = require('gulp-minify-css'), 
    //concat = require('gulp-concat'),
    uglify = require('gulp-uglify');


var srcCSS = 'front-end/css/*.css',
    distCSS = 'front-end/css/min/',
    srcJS = 'front-end/js/phyro/*.js', 
    distJS = 'front-end/js/';

gulp.task('styl', function(){
    gulp.src(srcCSS)
        .pipe(prefix(['safari 5', 'ff 21', 'ie 9', 'opera 12.1', 'ios 5', 'android 2.2'])) //
        .pipe(gulp.dest('front-end/css/prefixed/'))
        .pipe(minifycss())
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest(distCSS));
});

gulp.task('scripts', function(){
    gulp.src(srcJS)
        .pipe(uglify())
        //.pipe(concat('all.js'))
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest(distJS));
});

/*gulp.task('watch', function(){
    gulp.watch(srcCSS, ['styl']);
    gulp.watch(srcJS, ['scripts']);
    gulp.watch(srcJS, ['scripts']);
    gulp.watch(srcHtml, ['htmls'])
});*/
gulp.task('default', function(){
    console.log('Welcome from PhyroServer!');
    gulp.watch(srcCSS, ['styl']);
    gulp.watch(srcJS, ['scripts']);
});
