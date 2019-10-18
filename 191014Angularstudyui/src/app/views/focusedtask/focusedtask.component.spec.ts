import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { FocusedtaskComponent } from './focusedtask.component';

describe('FocusedtaskComponent', () => {
  let component: FocusedtaskComponent;
  let fixture: ComponentFixture<FocusedtaskComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FocusedtaskComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FocusedtaskComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
