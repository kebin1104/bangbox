//signup

// btn_top

$(document).ready(function(){
    $(window).scroll(function(){
        if($(this).scrollTop() > 500){
            $('#btn_top').fadeIn();
        }else{
            $('#btn_top').fadeOut();
        }
    });
 
    $('#btn_top').click(function () {
        $('html, body').animate({scrollTop: 0}, 450);
        return false;
    });
});

// delay - loading

  $(window).load(function () {
       $("#delay").fadeOut("slow");
   })

// scroll - effect

jQuery(document).ready(function($) {

			$("a.page-scroll").click(function(event){            
					var $anchor = $(this);
					$('html,body').stop().animate({
						scrollTop:$($anchor.attr('href')).offset().top
					}, 800);
					event.preventDefault();
			});
	});
	
	
	
	
$(document).ready(function(){
	$("#scroll").change(function(){
	  window.location.href = $(this).find("option:selected").attr("id");
	});
});
;

// header - more, push

function toggle_push_selection()
{
  var a = document.getElementById("menu_icon_push_mouseover");
       if(a.style.display == 'block')
          a.style.display = 'none';
       else
          a.style.display = 'block';
		  
	  
}


function toggle_more_selection()
{
  var b = document.getElementById("menu_icon_more_mouseover");
       if(b.style.display == 'block')
          b.style.display = 'none';
       else
          b.style.display = 'block';
}



// index - viewmode

  function viewmode(view)
        {
            if(view == 1)
            {
				$(".unbox_event").removeClass("view2");
				$(".unbox_event").addClass("view1");
				$(".unbox_event").css('width','60%');
				$(".event_user_info").css('display','block');
				$(".unbox_event:nth-child(2n)").css('margin','0 auto');
				$(".unbox_event:nth-child(2n)").css('margin-bottom','90px');
            } 
			else if(view == 2)
            {
				$(".unbox_event").removeClass("view1");
                $(".unbox_event").addClass("view2");
				$(".unbox_event:nth-child(2n)").css('margin-left','4%');
				$(".unbox_event:nth-child(2n)").css('margin-bottom','90px');
				$(".unbox_event").css('width','48%');
				$(".event_user_info").css('display','none');
            }
        }
// index - filter

function toggle_filter_selection()
{
  var e = document.getElementById("filter_selection");
       if(e.style.display == 'block')
          e.style.display = 'none';
       else
          e.style.display = 'block';
}



  $(document).ready(function(){
				   $(window).bind('scroll', function() {
				   var navHeight = $( window ).height() - 200;
						 if ($(window).scrollTop() > navHeight) {
							 $('.event_filter').addClass('fixed');
						 }
						 else {
							 $('.event_filter').removeClass('fixed');
						 }
					});
				});
				

;(function($)
{
    $.fn.checkAll = function (options)
    {
        var options = $.extend({
                scope: 'form',
                onMasterClick: null,
                onScopeChange: null
            }, options);

        return this.each(function() {

            var $master_checkbox = $(this),
                $scope = options.scope instanceof jQuery ? options.scope : $master_checkbox.closest(options.scope);

            $master_checkbox.on('click', function(e) {

                if ($master_checkbox.is(':checked'))
                    $scope.find('input[type="checkbox"]').not($master_checkbox).prop('checked', true).trigger('change');
                else
                    $scope.find('input[type="checkbox"]').not($master_checkbox).prop('checked', false).trigger('change');

                if (typeof options.onMasterClick === 'function')
                        options.onMasterClick($master_checkbox, $scope);
            });

            $scope.on('change', 'input[type="checkbox"]', function(e) {

                var $changed_checkbox = $(this);

                if ($changed_checkbox.is($master_checkbox))
                    return;

                if (typeof options.onScopeChange === 'function')
                        options.onScopeChange($master_checkbox, $changed_checkbox, $scope);

                if ( ! $changed_checkbox.is(':checked')) {
                    $master_checkbox.prop('checked', false);
                    return;
                }

                if ($scope.find('input[type="checkbox"]').not($master_checkbox).not(':checked').length === 0)
                    $master_checkbox.prop('checked', true);
                
            });
        });
    };
    
}(jQuery));


// event-page


function go_follow(){
	$('#follow_tag').html('팔로잉');	
	alert('팔로잉 하셨습니다.');
}

function price_1(num) {	
		var price_1 = 5000;	
		var total_price = price_1*num;
		$('#pay_price').html( '₩ '+total_price);
		$('#1st_ticket').html( '<option>1</option>');	
}

function go_join(){
	alert('신청되었습니다 :)');
}
// event-page - footer fixed

	$(document).ready(function(){
		$(window).bind('scroll', function() {
		   if($(this).scrollTop() > 500){
				 $('#footer').addClass('fixed');
				  $('#footer').fadeIn();
			 }
			 else {
				 $('#footer').removeClass('fixed');
				  $('#footer').fadeOut();
			 }
		});
	})


// search page

function go_search(){
	if($('#input_search').val() !=''){
		$('#search_result').show();	
		$('footer').show();	
	}else{
		alert('검색어를 입력해주세요');
		$('#search_result').hide();
		$('footer').hide();
	}
}

function delete_search(){
	$('#search_result').hide();
	$('#input_search').val('');
}




//follow-btn
 function following(){
			$(".follow_btn").css('backgroundcolor','#333');
				
        }



// radio - profile_LNB
$(document).ready(function() {

		// DOM 생성 완료 시 화면 숨김 (파라미터로 전달되는 id는 제외)
		hideExclude("profile1");

		// radio change 이벤트
		$("input[name=radioName]").change(function() {
			var radioValue = $(this).val();
			if (radioValue == "1") {
				hideExclude("profile1");
			} else if (radioValue == "2") {
				hideExclude("profile2");
			}
		});


		// 체크 되어 있는지 확인
		var checkCnt = $("input[name=radioName]:checked").size();
		if (checkCnt == 0) {
			// default radio 체크 (첫 번째)
			$("input[name=radioName]").eq(0).attr("checked", true);
		}

	});

	// text area 숨김
	function hideExclude(excludeId) {
		$("#changeArea").children().each(function() {
			$(this).hide();
		});

		// 파라미터로 넘겨 받은 id 요소는 show
		$("#" + excludeId).show();
	}

// unbox video
function video_player()
{
  var v = document.getElementById("menu_icon_push_mouseover");
       if(v.style.display == 'block')
          v.style.display = 'none';
       else
          v.style.display = 'block';
		  
	  
}



