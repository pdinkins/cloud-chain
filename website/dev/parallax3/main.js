/* 
See https://codepen.io/MarcelSchulz/full/lCvwq

The effect doens't appear as nice when viewing in split view :-)

Fully working version can also be found at (http://schulzmarcel.de/x/drafts/parallax).

*/

jQuery(document).ready(function(){
    $(window).scroll(function(e){
        parallaxScroll();
      });
       
      function parallaxScroll(){
          var scrolled = $(window).scrollTop();
          $('#parallax-bg-1').css('top',(0-(scrolled*.25))+'px');
          $('#parallax-bg-2').css('top',(0-(scrolled*.4))+'px');
          $('#parallax-bg-3').css('top',(0-(scrolled*.75))+'px');
      }
   
   }); 